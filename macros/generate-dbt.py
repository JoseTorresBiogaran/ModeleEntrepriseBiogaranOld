

def notifyMessage ( module, method, severity, message ):
    print ( module + " - " + method + " - " + repr(severity) + " - " + message )
    return

#Starting point
modutils = Modelio.getInstance().getModuleService().getPeerModule("ModelioUtils")
excelutils = Modelio.getInstance().getModuleService().getPeerModule("ExcelUtils")
cartomgr = Modelio.getInstance().getModuleService().getPeerModule("CartographyManager")
diagcol = Modelio.getInstance().getModuleService().getPeerModule("DiagramColorizer")
ormgen = Modelio.getInstance().getModuleService().getPeerModule("JavaOrmGenerator")
dbtgen = Modelio.getInstance().getModuleService().getPeerModule("DbtGenerator")
mn = modutils.getMessageNotifier ()
mn.subscribeListener ( notifyMessage )

tr = modutils.createTransaction ( "gendbt" )
dbtgen.setConfigTargetDatabase ( dbtgen.convertTargetDatabase ( "BigQuery" ) )
#clean the model from any DVB information
dbtgen.setConfigGenerateColumnNamesSnake ( True )
dbtgen.removeAllUmlArtefactsDBT ()
#deploy DVB selection information from 
useCases = modutils.createPairList ()
useCases.add ( modutils.createPair ( "Demo", "Sprint1") )
dbtgen.selectUmlArtefactsDBTFromUseCases ( useCases )
#dbtgen.selectAllUmlArtefactsDBT ()
#now deploy sprint names into the stallite names so that the incremental DVB config will happen smoothly
#so this will support federal enterprise model down to the DVB instance or data mesh (per usage) instances
#set the target path
oldpath=dbtgen.getConfigDBTPath  ()  
newpath = modutils.getFullPathFromPrefixedPath( "$(Workspace)\\DbtModel\\models\\dwh" )
dbtgen.setConfigDBTPath  ( newpath )  
#generate the DVB json files on disk
dbtgen.deployDBTConfiguration ()
#reset the path
dbtgen.setConfigDBTPath  ( oldpath )  
#dont memorize the selection
modutils.rollbackTransaction ( tr )
#modutils.closeTransaction ( tr )
