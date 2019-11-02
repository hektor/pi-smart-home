
import Signin from './views/Signin.svelte';
import About from './views/About.svelte';
import { writable } from 'svelte/store';
const router = {'/': Signin,'/sign-in': Signin,'/about': About}
export default router;export const curRoute = writable('/home');