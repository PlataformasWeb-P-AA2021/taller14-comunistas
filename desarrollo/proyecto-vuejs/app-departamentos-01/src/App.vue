<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-md-8">
        <h2><router-link to="/index">Administración de Estudiante</router-link></h2>
        <router-link to="/create_telefono" class="btn btn-sm btn-primary">Crear departamento</router-link>

        <router-view />
      </div>
    </div>
  </div>
</template>
