import csv
import pandas as pd
from pathlib import Path


def _students_name(class_name: str):
    names = []
    filtered_names = []
    students_dataset = Path("src/datasets/{}".format(class_name))
    students_ds = students_dataset.glob("*/*")

    for file_path in students_ds:
        name = file_path.parent.name
        names.append(name)

    [filtered_names.append(name)
     for name in names if name not in filtered_names]

    return filtered_names


def create_attendance_csv(class_name: str):
    attendance_folder = 'src/attendance/{}/attendance.csv'.format(class_name)
    names = _students_name(class_name)
    header_row = ['NAME']

    with open(attendance_folder, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        writer.writerow(header_row)

        for student in names:
            writer.writerow([student])


def check_attendance(class_name: str, students: list, attendance_ctr: int):
    attendance_folder = 'src/attendance/{}/attendance.csv'.format(class_name)
    names = _students_name(class_name)

    df = pd.read_csv(attendance_folder)

    for name in names:
        if name in students:
            df.loc[names.index(name), attendance_ctr] = "P"
            df.to_csv(attendance_folder, index=False)
        else:
            df.loc[names.index(name), attendance_ctr] = "A"
            df.to_csv(attendance_folder, index=False)


def generate_chart(class_name: str):
    attendance_folder = 'src/attendance/{}/attendance.csv'.format(class_name)

    df = pd.read_csv(attendance_folder)

    plot = (df.melt('NAME', value_name='STATUS')
            .value_counts(subset=['NAME', 'STATUS']).unstack()
            .plot.bar(stacked=True)
            )

    fig = plot.get_figure()
    
    chart_loc = 'src/attendance/{}/data.png'.format(class_name)

    fig.savefig(chart_loc)
    
    return chart_loc
