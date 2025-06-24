def notifyMessage ( module, method, severity, message ):
    print ( module + " - " + method + " - " + repr(severity) + " - " + message )
    return

#Starting point
modutils = Modelio.getInstance().getModuleService().getPeerModule("ModelioUtils")
excelutils = Modelio.getInstance().getModuleService().getPeerModule("ExcelUtils")
cartomgr = Modelio.getInstance().getModuleService().getPeerModule("CartographyManager")
diagcol = Modelio.getInstance().getModuleService().getPeerModule("DiagramColorizer")

mn = modutils.getMessageNotifier ()
mn.subscribeListener ( notifyMessage )

tm = modutils.createTypeMapper ()
td = tm.getTargetDatabaseFromString ( "BigQuery" )

print "Start generate SQL objects"
print modutils.getProjectStereotype ( "SqlPK" )
print modutils.getStereotypeProperties ( modutils.getProjectStereotype ( "SqlPK" ) )

genpath =  modutils.createFile ( modutils.markFileNameDate ( str(modutils.getWorkspacePath()) + "\\sql\\Retail_Finance_Sprint1" ) )
genpath.mkdirs()
useCases = modutils.createPairList ()
useCases.add ( modutils.createPair ( "Demo", "Sprint1") )
afuc = cartomgr.getArtefactsForUseCases ( useCases )

print genpath

for c in afuc.getClasses():
    sqltablename = modutils.getStereotypeInstValueString ( c.cls, modutils.getProjectStereotype ( "SQL" ), "TableName" )
    tablename = modutils.getUpperSqlNameFromJavaName ( c.cls.getName () )
    if modutils.isNullOrEmptyString ( sqltablename ) == False: tablename = sqltablename
    f = modutils.createFile ( genpath.getAbsolutePath () + "\\TABLE_" + tablename + ".ddl" )
    sb = modutils.createStringBuilder ()
    sb.append ( "create or replace TABLE " + tablename )
    desc = modutils.getDescription ( c.cls )
    if modutils.isNullOrEmptyString ( desc ) == False: sb.append ( " COMMENT = '" + modutils.cleanForSqlComment ( desc ) + "' " )
    sb.append ( "(\r" )
    for a in c.attributes:
        isPK = modutils.getStereotypeInstValue ( a, modutils.getProjectStereotype ( "SqlPK" ), "isPK" )
        colname = modutils.getUpperSqlNameFromJavaName ( a.getName () )
        sb.append ( "   " + colname + " " + tm.getDatabaseTypeFromUml ( a.getType().getName(), td ) ) 
        desc = modutils.getDescription ( a )
        if ( isPK == True ):
            if modutils.isNullOrEmptyString ( desc ) == False: 
                desc = desc + " - Primary Key"
            else:
                desc = "Primary Key"
        if modutils.isNullOrEmptyString ( desc ) == False: 
            sb.append ( " COMMENT '" + modutils.cleanForSqlComment ( desc ) + "'" )
        sb.append ( ",\r" )
    for a in c.associations:
        colname = modutils.getUpperSqlNameFromJavaName ( a.getName () )
        sb.append ( "   " + colname + " " + tm.getDatabaseTypeFromUml ( "string", td ) ) 
        desc = modutils.getDescription ( a )
        if modutils.isNullOrEmptyString ( desc ) == False:  
            sb.append ( " COMMENT 'Foreign Key : " + modutils.cleanForSqlComment ( desc ) + "'" )
        else:
            sb.append ( " COMMENT 'Foreign Key'" )
        sb.append ( ",\r" )
    il = sb.lastIndexOf ( ",\r" )    
    if il != -1: sb.deleteCharAt ( il )
    sb.append ( ")\r" )
    modutils.writeTextFile ( f, sb );    
    print "TABLE => " + f.getAbsolutePath ()
    

