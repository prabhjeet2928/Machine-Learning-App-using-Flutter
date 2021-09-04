import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:getwidget/getwidget.dart';

var output = "";
var age;
var pclass;
var sex;
var sibsp;
var embarked;
var parch;

class LogisticReg extends StatefulWidget {
  @override
  _LogisticRegState createState() => _LogisticRegState();
}

class _LogisticRegState extends State<LogisticReg> {
  web() async {
    var url = Uri.http("192.168.43.210", "cgi-bin/task11/logistic.py", {
      "age": age,
      "pclass": pclass,
      "sex": sex,
      "sibsp": sibsp,
      "embarked": embarked,
      "parch": parch
    });
    var response = await http.get(url);
    setState(() {
      output = response.body;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: Colors.black,
        body: SingleChildScrollView(
          child: Column(
            children: [
              Container(
                width: MediaQuery.of(context).size.width * 1.0,
                height: 300,
                decoration: BoxDecoration(
                    borderRadius:
                        BorderRadius.only(bottomLeft: Radius.circular(150.0)),
                    color: Colors.lightBlue.shade600),
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: <Widget>[
                    Center(
                      child: Container(
                        margin: EdgeInsets.only(left: 70),
                        alignment: Alignment.bottomRight,
                        width: 270,
                        height: 180,
                        child: Image.asset("assets/logistic_regression.png"),
                      ),
                    ),
                    Container(
                      margin: EdgeInsets.only(right: 25.0),
                      alignment: Alignment.bottomRight,
                      height: 70,
                      child: Text(
                        "Logistic Regression",
                        style: TextStyle(
                            fontSize: 28.0,
                            color: Colors.white,
                            fontWeight: FontWeight.bold),
                      ),
                    )
                  ],
                ),
              ),
              SizedBox(
                height: 40,
              ),
              Text("Used Titantic Dataset for Perdict is it Survived or not",
                  textAlign: TextAlign.center,
                  style: TextStyle(color: Colors.white, fontSize: 18.0)),
              SizedBox(
                height: 20,
              ),
              Container(
                child: TextField(
                  style: TextStyle(color: Colors.white),
                  onChanged: (value) {
                    age = value;
                  },
                  autocorrect: false,
                  textAlign: TextAlign.center,
                  decoration: InputDecoration(
                    hintText: "Enter Age (in float)",
                    hintStyle: TextStyle(color: Colors.white),
                    enabledBorder: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(20),
                        borderSide:
                            BorderSide(width: 2, color: Colors.lightBlue)),
                    focusedBorder: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(20),
                        borderSide:
                            BorderSide(width: 2, color: Colors.lightBlue)),
                  ),
                ),
              ),
              SizedBox(
                height: 20,
              ),
              Container(
                height: 58,
                width: MediaQuery.of(context).size.width,
                child: DropdownButtonHideUnderline(
                  child: GFDropdown(
                    isExpanded: true,
                    padding: EdgeInsets.all(15),
                    borderRadius: BorderRadius.circular(20),
                    border: BorderSide(color: Colors.blue, width: 2),
                    dropdownButtonColor: Colors.black,
                    dropdownColor: Colors.black,
                    style: TextStyle(color: Colors.white, fontSize: 17),
                    value: pclass,
                    iconEnabledColor: Colors.white,
                    hint: Center(
                      child: Text(
                        "Choose PClass",
                        style: TextStyle(color: Colors.white),
                      ),
                    ),
                    onChanged: (newValue) {
                      setState(() {
                        pclass = newValue;
                      });
                    },
                    items: [
                      "1",
                      "2",
                      "3",
                    ]
                        .map((value) => DropdownMenuItem(
                              value: value,
                              child: Center(
                                child: Text(
                                  value,
                                  style: TextStyle(color: Colors.white),
                                ),
                              ),
                            ))
                        .toList(),
                  ),
                ),
              ),
              SizedBox(
                height: 20,
              ),
              Container(
                height: 58,
                width: MediaQuery.of(context).size.width,
                child: DropdownButtonHideUnderline(
                  child: GFDropdown(
                    isExpanded: true,
                    padding: EdgeInsets.all(15),
                    borderRadius: BorderRadius.circular(20),
                    border: BorderSide(color: Colors.blue, width: 2),
                    dropdownButtonColor: Colors.black,
                    dropdownColor: Colors.black,
                    style: TextStyle(color: Colors.white, fontSize: 17),
                    value: sex,
                    iconEnabledColor: Colors.white,
                    hint: Center(
                      child: Text(
                        "Choose Gender",
                        style: TextStyle(color: Colors.white),
                      ),
                    ),
                    onChanged: (newValue) {
                      setState(() {
                        sex = newValue;
                      });
                    },
                    items: [
                      "male",
                      "female",
                    ]
                        .map((value) => DropdownMenuItem(
                              value: value,
                              child: Center(
                                child: Text(
                                  value,
                                  style: TextStyle(color: Colors.white),
                                ),
                              ),
                            ))
                        .toList(),
                  ),
                ),
              ),
              SizedBox(
                height: 20,
              ),
              Container(
                height: 58,
                width: MediaQuery.of(context).size.width,
                child: DropdownButtonHideUnderline(
                  child: GFDropdown(
                    isExpanded: true,
                    padding: EdgeInsets.all(15),
                    borderRadius: BorderRadius.circular(20),
                    border: BorderSide(color: Colors.blue, width: 2),
                    dropdownButtonColor: Colors.black,
                    dropdownColor: Colors.black,
                    style: TextStyle(color: Colors.white, fontSize: 17),
                    value: sibsp,
                    iconEnabledColor: Colors.white,
                    hint: Center(
                      child: Text(
                        "Choose SibSp",
                        style: TextStyle(color: Colors.white),
                      ),
                    ),
                    onChanged: (newValue) {
                      setState(() {
                        sibsp = newValue;
                      });
                    },
                    items: [
                      "0",
                      "1",
                      "2",
                      "3",
                      "4",
                      "5",
                      "8",
                    ]
                        .map((value) => DropdownMenuItem(
                              value: value,
                              child: Center(
                                child: Text(
                                  value,
                                  style: TextStyle(color: Colors.white),
                                ),
                              ),
                            ))
                        .toList(),
                  ),
                ),
              ),
              SizedBox(
                height: 20,
              ),
              Container(
                height: 58,
                width: MediaQuery.of(context).size.width,
                child: DropdownButtonHideUnderline(
                  child: GFDropdown(
                    isExpanded: true,
                    padding: EdgeInsets.all(15),
                    borderRadius: BorderRadius.circular(20),
                    border: BorderSide(color: Colors.blue, width: 2),
                    dropdownButtonColor: Colors.black,
                    dropdownColor: Colors.black,
                    style: TextStyle(color: Colors.white, fontSize: 17),
                    value: embarked,
                    iconEnabledColor: Colors.white,
                    hint: Center(
                      child: Text(
                        "Choose Embarked",
                        style: TextStyle(color: Colors.white),
                      ),
                    ),
                    onChanged: (newValue) {
                      setState(() {
                        embarked = newValue;
                      });
                    },
                    items: [
                      "C",
                      "Q",
                      "S",
                    ]
                        .map((value) => DropdownMenuItem(
                              value: value,
                              child: Center(
                                child: Text(
                                  value,
                                  style: TextStyle(color: Colors.white),
                                ),
                              ),
                            ))
                        .toList(),
                  ),
                ),
              ),
              SizedBox(
                height: 20,
              ),
              Container(
                height: 58,
                width: MediaQuery.of(context).size.width,
                child: DropdownButtonHideUnderline(
                  child: GFDropdown(
                    isExpanded: true,
                    padding: EdgeInsets.all(15),
                    borderRadius: BorderRadius.circular(20),
                    border: BorderSide(color: Colors.blue, width: 2),
                    dropdownButtonColor: Colors.black,
                    dropdownColor: Colors.black,
                    style: TextStyle(color: Colors.white, fontSize: 17),
                    value: parch,
                    iconEnabledColor: Colors.white,
                    hint: Center(
                      child: Text(
                        "Choose PArch",
                        style: TextStyle(color: Colors.white),
                      ),
                    ),
                    onChanged: (newValue) {
                      setState(() {
                        parch = newValue;
                      });
                    },
                    items: [
                      "0",
                      "1",
                      "2",
                      "3",
                      "4",
                      "5",
                      "6",
                      "9",
                    ]
                        .map((value) => DropdownMenuItem(
                              value: value,
                              child: Center(
                                child: Text(
                                  value,
                                  style: TextStyle(color: Colors.white),
                                ),
                              ),
                            ))
                        .toList(),
                  ),
                ),
              ),
              SizedBox(
                height: 40,
              ),
              Material(
                color: Colors.lightBlue.shade600,
                borderRadius: BorderRadius.circular(10),
                elevation: 10,
                child: MaterialButton(
                  textColor: Colors.white,
                  minWidth: 200,
                  height: 40,
                  child: Text("Submit", style: TextStyle(fontSize: 20.0)),
                  onPressed: web,
                ),
              ),
              SizedBox(
                height: 40,
              ),
              Text("${output}",
                  textAlign: TextAlign.center,
                  style: TextStyle(color: Colors.white, fontSize: 20.0)),
            ],
          ),
        ));
    ;
  }
}
