first run Spheroid_Analysis_merger_3_9_23

then run Spheroid_Analysis_Day_parser_3_9_23

optional: run Spheroid_Analysis_Day0_Filter if you want to eliminate dublets in the first day based on media area size

then run Spheroid_Analysis_all_days_parser_3_11_23

then run Spheroid_Analysis_duplicate_remover

finally, run Spheroid_Line_plotter_grouped

--- Note: the new "by_well" scripts parse objects by well, not image as before, due to a shuffeling of image/well order