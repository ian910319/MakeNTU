import 'package:flutter/material.dart';

class Picture extends StatelessWidget{
  @override
  Widget build(BuildContext context){
    return Scaffold(
      body: Column(
        children: [
          Container(
            constraints: BoxConstraints.expand(
              height: 360.0,
              width: 480.0,
            ),
            decoration: BoxDecoration(color: Colors.grey),
            child: Image.asset(
              "assets/images/graph.png",
              
              fit: BoxFit.cover,
            ),
          ),
          Text("Patient activity", style: TextStyle(fontSize: 24),),
          Text("(Each circle is one day.)", style: TextStyle(fontSize: 20),),
          Text("   Redder area represent higher activity.", style: TextStyle(fontSize: 20),),
          Text("    It allows caretaker to speculate the \n    lifestyle and monitor health condition\n    of this patient.\n", style: TextStyle(fontSize: 20),),
        ],
      ),
    );
  }
}