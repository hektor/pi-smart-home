import firebase from "firebase/app";
import "firebase/auth";
import "firebase/firestore";

import { authState } from 'rxfire/auth';
import { collectionData } from 'rxfire/firestore';

const firebaseConfig = {
  apiKey: "AIzaSyCLv2oNEww2yH7_gwXl71qGQzzO5wAu1cI",
  authDomain: "pi-smart-hub.firebaseapp.com",
  databaseURL: "https://pi-smart-hub.firebaseio.com",
  projectId: "pi-smart-hub",
  storageBucket: "pi-smart-hub.appspot.com",
  messagingSenderId: "842019025116",
  appId: "1:842019025116:web:6d8b70ea26a4d61daf8419"
};

firebase.initializeApp(firebaseConfig);

const auth = firebase.auth();
const googleProvider = new firebase.auth.GoogleAuthProvider();
const firestore = firebase.firestore();

export { auth, googleProvider, firestore }
