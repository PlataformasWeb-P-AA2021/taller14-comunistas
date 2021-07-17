<template>
    <div class="pt-5">
        <form @submit.prevent="create" method="post">
            <div class="form-group">
                <label for="propietario">Nombre del Propietario</label>
                <input
                    type="text"
                    class="form-control"
                    id="propietario"
                    v-model="departamento.propietario"
                    v-validate="'required'"
                    name="propietario"
                    placeholder="Ingrese propietario"
                    :class="{'is-invalid': errors.has('departamento.propietario') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid name.
                </div>
            </div>

            <div class="form-group">
                <label for="costoDep">Costo</label>
                <input
                    type="number"
                    class="form-control"
                    id="costoDep"
                    v-model="departamento.costoDep"
                    v-validate="'required'"
                    name="costoDep"
                    placeholder="Ingrese Tipo"
                    :class="{'is-invalid': errors.has('departamento.costoDep') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid apellido.
                </div>
            </div>

            <div class="form-group">
                <label for="numCuartos">Numero de cuartos</label>
                <input
                    type="number"
                    class="form-control"
                    id="numCuartos"
                    v-model="departamento.numCuartos"
                    v-validate="'required'"
                    name="numCuartos"
                    placeholder="Ingrese Tipo"
                    :class="{'is-invalid': errors.has('departamento.numCuartos') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid apellido.
                </div>
            </div>

            <div class="form-group">
              <br>
                <label for="edificio">Edificio</label>
                <select v-model="departamento.edificio">
                            <option v-for="e in edificiosList" :key="e.url" :value="e.url">{{ e.nombre }}</option>
                        </select>
            </div>
            <br>
            <button type="submit" class="btn btn-primary">Crear</button>
        </form>
    </div>
</template>

<script>

import axios from 'axios';

export default {
    data() {
        return {
            departamento: {
                propietario: '',
                tipo: '',
                numCuartos: '',
                edificio: '',
            },
            edificiosList: [],
            submitted: false
        }
    },
    mounted() {
        this.getedificiosList()
    },
    methods: {
      getedificiosList() {
            axios
            .get('http://127.0.0.1:8000/api/edificios/')
            .then(response => {
                this.edificiosList = response.data
            })
            .catch(error => {
                console.log(error)
            })

        },
        create: function (e) {
            this.$validator.validate().then(result => {
                this.submitted = true;
                if (!result) {
                    return;
                }
                axios.post('http://127.0.0.1:8000/api/departamentos/',
                        this.departamento
                    )
                    .then(response => {
                        this.$router.push('/');
                    })
            });
        }
    },
}
</script>
