  // Firebase
  import { auth, googleProvider, firestore } from '../firebase'
  import { authState } from 'rxfire/auth'

   /**
    * TODO: Create
    */

    const saveMatrix = async (name, matrix) => {
      firestore.collection('matrices').add({name: name, matrix: matrix})
    }

      /**
   * TODO: Get all from document
   */

   const getAllFromDocument = async (collection, document) => {
    let ref = await firestore
    .collection(collection)
    .doc(document)
    .get()
    let data = await ref.data();
    return data;
   }

   const getAlarmStatus = async () => {
    let ref = await firestore.collection("devices").doc("sensors").get();
    let data = await ref.data();
    return data;
   }

   /**
    * TODO: Update
    */

    const toggleAlarm = async () => {
        let alarmStatus = await getAlarmStatus()
        alarmStatus = alarmStatus.breach
        firestore.collection("devices").doc("sensors").update({
          breach: !alarmStatus
      });
    }

    /**
     * TODO: Delete
     */

export { getAllFromDocument, toggleAlarm, getAlarmStatus, saveMatrix }