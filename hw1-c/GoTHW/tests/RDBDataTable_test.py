from src.data_tables.RDBDataTable import RDBDataTable
import json
import pymysql


connect_info = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'rv8855741',
    'db': 'W4111GoTSolutionClean',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

def t1():

    print("\n************** t1 **************\n")

    tbl = RDBDataTable("W4111GoTSolutionClean.episdes", connect_info=connect_info)
    print("Table = ", tbl)
    print("\n")
    tbl = RDBDataTable("W4111GoTSolutionClean.episodes")
    print("Table = ", tbl)

    print("\n************** t1 **************\n")


def t2():

    print("\n************** t2 **************\n")

    tbl = RDBDataTable("W4111GoTSolutionClean.episodes")

    res = tbl.find_by_template(
        {"seasonNum": 1},
        field_list=['seasonNum', 'episodeNum', 'episodeTitle']
    )

    print("Answer = ")
    print(json.dumps(res, indent=2, default=str))

    print("\n************** t2 **************\n")


def t3():


    print("\n************** t3 **************\n")

    tbl = RDBDataTable("W4111GoTSolutionClean.scenes")

    res = tbl.find_by_primary_key([3,1, 11],
        field_list=['seasonNum', 'episodeNum', 'sceneNo', "location", "subLocation"]
    )

    print("Answer = \n")
    print(json.dumps(res, indent=2, default=str))


    print("\n************** t3 **************\n")


# def t4():
#
#     print("\n************** t4 **************\n")
#     dbs = RDBDataTable.get_folders()
#     print("dbs = ", json.dumps(dbs, indent=2))
#     print("\n")
#
#     tbls = RDBDataTable.get_folders(dbname="W4111GoTSolutionClean")
#     print("tbls = ", json.dumps(tbls, indent=2))
#     print("\n************** t4 **************\n")
#
#
# def t5():
#
#     print("\n************** t5 **************\n")
#
#     tbl = RDBDataTable("W4111GoTSolutionClean.scenes")
#
#     k = tbl.get_key_columns()
#     print("Key columns = ", k)
#
#     print("\n************** t5 **************\n")



t1()
t2()
t3()
# t4()
# t5()