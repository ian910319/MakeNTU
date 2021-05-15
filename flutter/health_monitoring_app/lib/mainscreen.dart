import 'package:flutter/material.dart';
import 'patient.dart';

class MainScreen extends StatelessWidget{
  @override
  Widget build(BuildContext context){
    return Scaffold(
      appBar: AppBar(
        leading: IconButton(icon: Icon(Icons.menu), onPressed:(){}
        
        ),
        title: Text("Healthcaring System", style: TextStyle(fontSize: 24.0)),
        actions: <Widget>[
          IconButton(icon: Icon(Icons.search), onPressed:(){

          }),
        ]
      ),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.start,
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          Patient('Patient 1:Ian Chiang'),
          Patient('Patient 2:Chiang Cheng-En'),
          Patient('Patient 3:江承恩'),
        ]
      )
    );
  }
}