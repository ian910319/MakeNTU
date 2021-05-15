import 'package:flutter/material.dart';
import 'patientdata.dart';

class Patient extends StatelessWidget{
  String _text;

  Patient(String text,) {
    this._text = text;
  }

  @override
  Widget build(BuildContext context){
    return RaisedButton(
      child: Text(_text,
      style: TextStyle(color: Colors.white, fontSize: 24.0),

      ),
      color: Colors.blueGrey,
      onPressed: (){
        Navigator.push(context, MaterialPageRoute(builder: (context)=>PatientData()));
      },
    );
  }
}