import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      redirect: '/index'
    },
    {
       path: "/edit/:id",
       name: "edit",
       component: () => import("./components/Edit.vue")
     },
    {
      path: "/index",
      name: "index",
      component: () => import("./components/Index.vue")
    },
    {
      path: "/create_telefono",
      name: "create_telefono",
      component: () => import("./components/CreateDepartamento.vue")
    },
  ]
});
