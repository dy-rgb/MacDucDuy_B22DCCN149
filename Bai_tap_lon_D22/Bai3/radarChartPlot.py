import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import argparse
from math import pi

def load_data(file_path):
    """Đọc dữ liệu từ file CSV."""
    data = pd.read_csv(file_path)
    return data

def get_player_data(data, player_name, attributes):
    """Lấy dữ liệu của cầu thủ với các thuộc tính được chọn."""
    player_data = data[data['Name'] == player_name]
    if player_data.empty:
        raise ValueError(f"Không tìm thấy cầu thủ '{player_name}' trong dữ liệu.")
    return player_data[attributes].values.flatten()

def plot_radar_chart(player1_name, player2_name, attributes):
    """Vẽ biểu đồ radar so sánh hai cầu thủ với các thuộc tính đã chọn."""
    # Đọc dữ liệu từ file
    data = load_data('results.csv')

    # Lấy dữ liệu của hai cầu thủ
    player1_data = get_player_data(data, player1_name, attributes)
    player2_data = get_player_data(data, player2_name, attributes)

    # Số lượng thuộc tính
    num_vars = len(attributes)

    # Góc cho mỗi trục
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

    # Bố trí dữ liệu cho radar chart
    player1_data = np.concatenate((player1_data, [player1_data[0]]))
    player2_data = np.concatenate((player2_data, [player2_data[0]]))
    angles += angles[:1]

    # Tạo biểu đồ radar
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

    # Vẽ dữ liệu của cầu thủ 1
    ax.fill(angles, player1_data, color="red", alpha=0.25)
    ax.plot(angles, player1_data, color="red", linewidth=2, label=player1_name)

    # Vẽ dữ liệu của cầu thủ 2
    ax.fill(angles, player2_data, color="blue", alpha=0.25)
    ax.plot(angles, player2_data, color="blue", linewidth=2, label=player2_name)

    # Cài đặt nhãn
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(attributes)

    # Hiển thị biểu đồ
    plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
    plt.title(f"So sánh giữa {player1_name} và {player2_name}")
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Biểu đồ Radar so sánh cầu thủ")
    parser.add_argument("--p1", required=True, help="Tên cầu thủ thứ nhất")
    parser.add_argument("--p2", required=True, help="Tên cầu thủ thứ hai")
    parser.add_argument("--Attribute", required=True, help="Danh sách các thuộc tính cần so sánh, cách nhau bởi dấu phẩy")

    args = parser.parse_args()
    player1_name = args.p1
    player2_name = args.p2
    attributes = args.Attribute.split(',')

    plot_radar_chart(player1_name, player2_name, attributes)

# python D:\Bai_tap_lon_D22\Bai3\radarChartPlot.py --p1 "Kevin De Bruyne" --p2 "Virgil van Dijk" --Attribute "Playing time_Matches played,Progression_PrgC,Shooting_Standard_SoT%,Passing_Long_Cmp,Pass Types_Pass Types_Dead"