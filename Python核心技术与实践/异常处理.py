# -*- coding:utf8 -*-
# @Time：2021/11/11 10:03 上午
# @Author： Huang Jeff
import sys

# try:
#     f = open('file.txt', 'r')
# except OSError as err:
#     print('OS error: {}'.format(err))
# except BaseException:
#     print('Unexpected error:', sys.exc_info()[0])
# finally:
#     f.close()

try:
    10 / 0
    # order * 2
    # 1 + [1, 2]
# except OSError as err:
# except ValueError as err:
except (ValueError, IndexError) as err:
    print('Error:{}'.format(err))

# 数据库连接异常检测方法
try:
    db = DB.connect('<db path>')
    raw_data = DB.queryData('<viewer_id>')
except (DBConnectionError, DBQueryDataError) as err:
    print('Error: {}'.format(err))
