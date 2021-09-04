import 'package:flutter/material.dart';
import 'package:ml_app/Credentials/home.dart';
import 'package:easy_splash_screen/easy_splash_screen.dart';

class MySplash extends StatefulWidget {
  @override
  _MySplashState createState() => _MySplashState();
}

class _MySplashState extends State<MySplash> {
  @override
  Widget build(BuildContext context) {
    return EasySplashScreen(
      logo: Image.asset("assets/ml_logo.gif"),
      title: Text(
        "ML App",
        style: TextStyle(
          fontSize: 38,
          fontWeight: FontWeight.bold,
          color: Colors.blue,
        ),
      ),
      backgroundColor: Colors.black,
      showLoader: true,
      navigator: AfterSplash(),
      durationInSeconds: 8,
      logoSize: 60,
      loaderColor: Colors.blue,
      loadingText: Text(
        "     from\nEpic Dream",
        style: TextStyle(
            fontWeight: FontWeight.w600, color: Colors.white, fontSize: 20),
      ),
    );
  }
}

class AfterSplash extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MyHome();
  }
}
