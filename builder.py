import os
import cach
import database
import fn
import config as cn
import model.tableInfo as tableInfo
import plugin



class builder(object):
    cr = None
    db = None
    instance=None
    obj={}



    @classmethod
    def getInstance(cls):
        if cls.instance is None:
            cls.instance=builder()
            return cls.instance
        else:
            return cls.instance


    def build(self,obj):
        self.obj=obj
        self.db = database.getInstance().getDb()
        self.cr=cach.getInstance()
        for key in self.obj:
            if dir in self.handler:
                self.handler[key](self)
        self.db.close()


    def controller(self):
        1
    def service(self):
        1
    def dao(self):
        1
    def po(self):
        cursor = self.db.cursor()
        cr = self.cr
        filePath = cr.get("packagePath") + "po\\"
        cursor.execute("select TABLE_NAME from INFORMATION_SCHEMA.TABLES  where TABLE_SCHEMA='supervisory'")

        for item in cursor.fetchall():
            for key in item:
                bean = self.getTableInfo(item["TABLE_NAME"])
                package = cr.get("package")
                lines = fn.readAsLines(cn.FILEPATH.PO.value + "po")
                file = fn.openFile(filePath + bean.getPoName() + ".java")
                for s in lines:
                    file.write(
                        s.replace("$PACKAGE", package).replace('$AUTHNOTE', fn.authNote(bean.getComment())).replace(
                            "$TABLENAME", bean.getTableName())
                            .replace("$PONAME", bean.getPoName()).replace("$MAIN",bean.getColCode()).replace("$IMPORT",bean.getRel()))
                file.close()

    def getTableInfo(self,tableName):
        cursor = database.getInstance().getDb().cursor()
        comment = None

        ta = tableInfo.tableInfo()
        ta.setTableName(tableName)
        ta.setPoName(fn.underline2Camel(tableName))

        sql = "SELECT TABLE_COMMENT FROM INFORMATION_SCHEMA.TABLES  WHERE TABLE_NAME = '%s' AND TABLE_SCHEMA = '%s'" % (
        tableName, "supervisory")
        cursor.execute(sql)
        temp = cursor.fetchone()
        if temp is not None:
            for i in temp:
                comment = temp[i]
        ta.setComment(comment)

        sql = "SELECT  column_name  AS 'name',column_key AS 'key',data_type  AS 'type' ,character_maximum_length AS 'strLen',numeric_precision AS 'numLen'  , numeric_scale  , +" \
              "is_nullable 'nullable', CASE   WHEN extra = 'auto_increment' THEN 1  ELSE 0   END AS 'increment',  column_default   as 'defalut' ,   +" \
              "column_comment    as 'comment'  FROM  Information_schema.columns  WHERE   +" \
              "table_Name='%s'" % tableName
        cursor.execute(sql)

        temp = []
        relArr=[]
        for item in cursor.fetchall():
            if item["strLen"]:
                length = item["strLen"]
            else:
                length = item["numLen"]

            if length is None:
                lenStr=")"
            else:
                lenStr=", length = %d)" %length

            transType= cn.TYPEMAP.MYSQL2JAVA.value[item["type"]]["type"]
            rel=cn.TYPEMAP.MYSQL2JAVA.value[item["type"]]["rel"]
            if rel !="":
                relArr.append(rel)

            ex = "%s" % fn.titleNote(item['comment']) + \
                 "    @Column(name = '%s'" % item["name"] +lenStr  + "\n" + "    private %s %s;" % (transType, fn.underline2Camel(item["name"])) + "\n"
            if item["key"] == "PRI":
                temp.insert(0, ex)
            else:
                temp.append(ex)
        ta.setColCode("".join(temp))
        ta.setRel("".join(list(set(relArr))))

        return ta

    def config(self):
        1

    def repository(self):
        1

    def annotation(self):
        1

    def filter(self):
        1

    def util(self):
        1

    def searchModel(self):
        if "swagger" in self.cr.get("plugin"):
            tar="swaggerPage"
        else:
            tar="pageParam"
        plugin.getInstance().apply(["swagger"])
        package = self.cr.get("package")
        file = fn.openFile(self.cr.get("packagePath")+"searchModel\\"+"PageParamModel.java")
        lines=fn.readAsLines(cn.FILEPATH.SEARCHMODEL.value+tar)
        for s in lines:
            file.write(
                s.replace("$PACKAGE", package).replace('$AUTHNOTE',fn.authNote("分页容器"))
            )
        file.close()






    handler = {
        "controller": controller,
        "service": service,
        "dao": dao,
        "po": po,
        "config": config,
        "repository": repository,
        "annotation": annotation,
        "filter": filter,
        "util": util,
        "searchModel":searchModel
    }


def getInstance():
    return builder.getInstance()


