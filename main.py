import os
import pandas as pd
from matplotlib import pyplot as plt
import datetime

url = "https://ai-process-sandy.s3.eu-west-1.amazonaws.com/purge/deviation.json"
file_path = "deviation.json"
now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
dataframe = pd.read_json(url)
dataframe.to_json(file_path)


class PlotDrawer:
    def __init__(self):
        self.plots_folder = "plots"
        if not os.path.exists(self.plots_folder):
            os.makedirs(self.plots_folder)

    def read_json_file(self, json_file_path):
        df = pd.read_json(json_file_path)
        return df

    def draw_plots(self, df):
        plt.plot(df['rb_corners'], label='Model Predictions')
        plt.plot(df['gt_corners'], label='Ground Truth')
        plt.xlabel('Комната')
        plt.ylabel('Количество углов')
        plt.legend()
        plt.savefig(f'{self.plots_folder}/corners_comparison - {now}.png')
        plt.close()

        plots_paths = [f'{self.plots_folder}/corners_comparison - {now}.png']
        return plots_paths


plot_drawer = PlotDrawer()
df = plot_drawer.read_json_file(file_path)
plots_paths = plot_drawer.draw_plots(df)
print(plots_paths)
