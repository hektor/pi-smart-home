  // Firebase
  import { auth, googleProvider, firestore } from '../firebase'
  import { authState } from 'rxfire/auth'

   /**
    * TODO: Create
    */

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

   /**
    * TODO: Update
    */

    /**
     * TODO: Delete
     */

export { getAllFromDocument }