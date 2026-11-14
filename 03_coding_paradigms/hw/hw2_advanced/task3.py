# task3.py — Домашняя работа 10, продвинутый уровень.
# Задача 3. Аналитическая визуализация (matplotlib + seaborn).


# ============================================================
# Задача 3. Аналитическая визуализация
# ============================================================
# Создаём набор аналитических графиков по таблице заказов df
# со столбцами "city", "category", "price", "revenue".
#
# Подзадачи:
#   3.1. Построить sns.scatterplot(data=df, x="price", y="revenue", hue="category", ax=ax)
#        с заголовком "Price vs Revenue". Вернуть ax.
#   3.2. Построить sns.boxplot(data=df, x="city", y="revenue", ax=ax)
#        с заголовком "Revenue by City" и подписью оси Y "Revenue". Вернуть ax.
#   3.3. Построить дашборд из двух графиков fig, axes = plt.subplots(1, 2, figsize=(10, 4)):
#        - на axes[0]: столбчатый график суммарной выручки по городам
#          с заголовком "Total by City";
#        - на axes[1]: гистограмма столбца "revenue" с заголовком "Revenue Hist".
#        Вернуть кортеж (fig, axes).
#   3.4. Построить дашборд из 3.3, сохранить фигуру в out_path (dpi=120),
#        закрыть фигуру через plt.close(fig) и вернуть размер файла в байтах.

import os
import tempfile

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def hw_3_1_scatter_by_category(df: pd.DataFrame):
    """Построить диаграмму рассеяния с раскраской hue='category' и вернуть ax."""
    # TODO: реализовать
    pass


def hw_3_2_city_boxplot(df: pd.DataFrame):
    """Построить boxplot выручки по городам и вернуть ax."""
    # TODO: реализовать
    pass


def hw_3_3_dashboard(df: pd.DataFrame):
    """Построить панель (1, 2) с суммой по городам и гистограммой, вернуть (fig, axes)."""
    # TODO: реализовать
    pass


def hw_3_4_export_dashboard(df: pd.DataFrame, out_path: str) -> int:
    """Сохранить дашборд в out_path (dpi=120), закрыть фигуру и вернуть размер файла."""
    # TODO: реализовать
    pass


# ============================================================
# Assert-тесты
# ============================================================

if __name__ == "__main__":
    sample_df = pd.DataFrame({
        "city": ["Berlin", "Berlin", "Munich", "Munich", "Hamburg"],
        "category": ["Books", "Tech", "Tech", "Books", "Tech"],
        "price": [20.0, 500.0, 700.0, 35.0, 450.0],
        "revenue": [60.0, 500.0, 1400.0, 70.0, 900.0],
    })

    ax_sc = hw_3_1_scatter_by_category(sample_df)
    assert ax_sc.get_title() == "Price vs Revenue"

    ax_bx = hw_3_2_city_boxplot(sample_df)
    assert ax_bx.get_title() == "Revenue by City"
    assert ax_bx.get_ylabel() == "Revenue"

    fig_d, axes_d = hw_3_3_dashboard(sample_df)
    assert len(axes_d) == 2
    assert axes_d[0].get_title() == "Total by City"
    assert axes_d[1].get_title() == "Revenue Hist"
    plt.close("all")

    with tempfile.TemporaryDirectory() as tmpdir:
        png_path = os.path.join(tmpdir, "dashboard.png")
        size_bytes = hw_3_4_export_dashboard(sample_df, png_path)
        assert size_bytes > 1000 and os.path.exists(png_path)

    print("task3 (hw2_advanced): все assert-тесты пройдены.")
