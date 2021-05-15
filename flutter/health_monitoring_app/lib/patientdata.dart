import 'package:flutter/material.dart';
import 'picture.dart';
import 'warning.dart';

class PatientData extends StatefulWidget{
  PatientData({Key key}) : super(key: key);

  @override
  _PatientDataState createState() => _PatientDataState();
}

class _PatientDataState extends State<PatientData>{
  int _selectitems = 0;
  var _pages = [Picture(),Warning()];
  var _pageController = PageController();

  @override
  Widget build(BuildContext context){
    return Scaffold(
      appBar: AppBar(
        title: Text("Patient's Data",style: TextStyle(fontSize: 24.0),),
      ),
      body: PageView(
        children: _pages,
        onPageChanged: (index){
          setState(() {
            _selectitems = index;
          });
        },
        controller: _pageController,
      ),
      bottomNavigationBar: BottomNavigationBar(
        items: <BottomNavigationBarItem>[
          BottomNavigationBarItem(icon: Icon(Icons.image_rounded), title: Text('Graph')),
          BottomNavigationBarItem(icon: Icon(Icons.report_problem_rounded), title: Text('Warning'))
        ],
        currentIndex: _selectitems,
        onTap: (index) {
          setState(() {
            _selectitems = index;
            _pageController.animateToPage(_selectitems,
              duration: Duration(milliseconds: 200), 
              curve: Curves.linear);
          });
        }
      ),
    );
  }
}