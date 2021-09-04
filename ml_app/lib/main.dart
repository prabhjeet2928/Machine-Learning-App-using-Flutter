import 'package:flutter/material.dart';
import 'splashscreen/splashscreendata.dart';
import 'Credentials/registration.dart';
import 'Credentials/login.dart';
import 'Credentials/home.dart';
import 'ML_Screens/ml.dart';
import 'ML_Screens/linear.dart';
import 'ML_Screens/multilinear.dart';
import 'ML_Screens/logistic.dart';
import 'ML_Screens/kmeans.dart';
import 'ML_Screens/knn.dart';
import 'ML_Screens/random.dart';
import 'ML_Screens/decision.dart';
import 'ML_Screens/naivebayes.dart';
import 'package:firebase_core/firebase_core.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  Firebase.initializeApp();
  runApp(MaterialApp(
    initialRoute: "mysplash",
    debugShowCheckedModeBanner: false,
    routes: {
      "mysplash": (context) => MySplash(),
      "home": (context) => MyHome(),
      "ml": (context) => MyML(),
      "reg": (context) => MyReg(),
      "login": (context) => MyLogin(),
      "linear": (context) => LinearReg(),
      "multilinear": (context) => MultiLinearReg(),
      "logistic": (context) => LogisticReg(),
      "kmeans": (context) => KMeansCluster(),
      "knn": (context) => KNNClass(),
      "random": (context) => RandomForest(),
      "decision": (context) => DecisionTree(),
      "naive": (context) => NaiveBayesClass(),
    },
  ));
}
