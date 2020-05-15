from core.apply_dict import process
from regulation_dict.kunlun_regulation import get_kunlun_regulations
from regulation_dict.vins_additional_regulation import vins_additional_regulation
import os
from sys import argv

if(len(argv) < 2):
    print("example: python main.py v12.log")
    quit()

log_filename = argv[1]
output_bagname = os.path.splitext(log_filename)[0] + '.bag'
# regulations = get_kunlun_regulations()
regulations = vins_additional_regulation()
process(log_filename, regulations, output_bagname)