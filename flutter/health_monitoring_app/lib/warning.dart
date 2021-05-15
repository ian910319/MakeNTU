import 'package:flutter/material.dart';
import 'package:flutter/services.dart' show rootBundle;

class Warning extends StatefulWidget{
  @override
  _WarningState createState() => _WarningState();
}

class _WarningState extends State<Warning>{

  String data = '';
  fetchFileData() async{
    String responseText;
    responseText = await rootBundle.loadString('assets/text/warning.txt');

    setState(() {
      data = responseText;
    });
  }
  @override
  void initState(){
    fetchFileData();
    super.initState();
  }

  @override
  Widget build(BuildContext context){
    return Scaffold(
      body: Container(
        child: Align(
          alignment: Alignment.topLeft,
          child: Text(data, style: TextStyle(fontSize: 24.0)),
        ),
      ),
    );
  }
}