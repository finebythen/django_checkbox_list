from django.shortcuts import render, redirect
from django_pandas.io import read_frame
from gapminder import gapminder
import numpy as np
import pandas as pd
import json

from .models import GapminderObjects


def main(request):
    # load gapminder data and add additional content
    df = gapminder
    df['id_count'] = list(range(1, df.shape[0] + 1))

    # convert dataframe to json (for template)
    json_raw_df = df.to_json(orient='records')
    json_df = json.loads(json_raw_df)

    if request.method == 'POST':
        # get all checked data in table
        checked_data = request.POST.getlist('list_gap')

        for item in checked_data:
            df_filter = df.loc[df['id_count'] == int(item)]
            df_row = df_filter.values.tolist()

            # create items for model-save
            mdl_01 = item
            mdl_02 = df_row[0][0]
            mdl_03 = df_row[0][1]
            mdl_04 = str(df_row[0][2])
            mdl_05 = str(request.user)

            # create model
            qs_gap = GapminderObjects(
                id_gapminder=mdl_01,
                country=mdl_02,
                continent=mdl_03,
                year=mdl_04,
                user_created=mdl_05
            )
            # save in model
            qs_gap.save()

        return redirect("Main")

    context = {'json_df': json_df}
    return render(request, 'app_cckbx/main.html', context)
