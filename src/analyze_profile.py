import pstats

p = pstats.Stats('profiling_data.prof')
p.sort_stats('time').print_stats()