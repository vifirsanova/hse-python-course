# task3.py — Домашняя работа 10, базовый уровень.
# Задача 3. Построение базовых графиков (matplotlib и seaborn).


# ============================================================
# Задача 3. Построение базовых графиков
# ============================================================
# Тренируемся создавать типовые графики с подписями осей и сохранением.
#
# Подзадачи:
#   3.1. Построить линейный график days vs temps с заголовком "Temperature",
#        подписью оси X "Day" и оси Y "Celsius". Вернуть ax.
#   3.2. Построить столбчатую диаграмму cities vs counts с заголовком "Users".
#        Вернуть ax.
#   3.3. Построить гистограмму sns.histplot(data=df, x=col, bins=bins, ax=ax)
#        с заголовком f"Distribution of {col}". Вернуть ax.
#   3.4. Сохранить переданную фигуру fig в файл out_path и вернуть True,
#        если файл успешно записан и имеет размер > 0 байт.

import os
import tempfile

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def hw_3_1_line_chart(days: list[int], temps: list[float]):
    """Построить линейный график температуры и вернуть ax."""
    # TODO: реализовать
    pass


def hw_3_2_bar_chart(cities: list[str], counts: list[int]):
    """Построить столбчатый график с заголовком 'Users' и вернуть ax."""
    # TODO: реализовать
    pass


def hw_3_3_hist_chart(df: pd.DataFrame, col: str, bins: int = 5):
    """Построить sns.histplot по столбцу col и вернуть ax."""
    # TODO: реализовать
    pass


def hw_3_4_save_figure(fig, out_path: str) -> bool:
    """Сохранить fig в out_path и проверить, что файл непустой."""
    # TODO: реализовать
    pass


# ============================================================
# Assert-тесты
# ============================================================

if __name__ == "__main__":
    ax1 = hw_3_1_line_chart([1, 2, 3], [15.0, 18.5, 17.0])
    assert ax1.get_title() == "Temperature"
    assert ax1.get_xlabel() == "Day" and ax1.get_ylabel() == "Celsius"
    assert len(ax1.lines) == 1

    ax2 = hw_3_2_bar_chart(["Berlin", "Paris"], [120, 95])
    assert ax2.get_title() == "Users" and len(ax2.patches) == 2

    df_scores = pd.DataFrame({"score": [50, 60, 70, 80, 90, 95, 100]})
    ax3 = hw_3_3_hist_chart(df_scores, "score", bins=4)
    assert ax3.get_title() == "Distribution of score"

    with tempfile.TemporaryDirectory() as tmpdir:
        target = os.path.join(tmpdir, "out.png")
        assert hw_3_4_save_figure(ax1.figure, target) is True
        assert os.path.exists(target) and os.path.getsize(target) > 0

    plt.close("all")
    print("task3 (hw2_basic): все assert-тесты пройдены.")
