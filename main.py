
import time_series_visualizer

# Test all visualizations
print("Drawing line plot...")
line_fig = time_series_visualizer.draw_line_plot()
print("Line plot saved as line_plot.png")

print("Drawing bar plot...")
bar_fig = time_series_visualizer.draw_bar_plot()
print("Bar plot saved as bar_plot.png")

print("Drawing box plots...")
box_fig = time_series_visualizer.draw_box_plot()
print("Box plots saved as box_plot.png")

print("All visualizations completed successfully!")

# Run unit tests (if available)
# from unittest import main
# main(module='test_module', exit=False)
