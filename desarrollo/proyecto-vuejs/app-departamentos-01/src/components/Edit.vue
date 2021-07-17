<template>
    <div class="pt-5">
        <form @submit.prevent="update" method="post">
            <div class="form-group">
                <label for="propietario">propietario</label>
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
                    name="costoDep"
                    class="form-control"
                    id="costoDep"
                    v-validate="'required'"
                    v-model="departamento.costoDep"
                    cols="30"
                    rows="2"
                    :class="{'is-invalid': errors.has('departamento.costoDep') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid description.
                </div>
            </div>
            <div class="form-group">
                <label for="numCuartos">Numero de cuartos</label>
                <input
                    name="numCuartos"
                    class="form-control"
                    id="numCuartos"
                    v-validate="'required'"
                    v-model="departamento.numCuartos"
                    cols="30"
                    rows="2"
                    :class="{'is-invalid': errors.has('departamento.numCuartos') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid description.
                </div>
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
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
                costoDep: '',
                cedula: '',
                correo: '',
                url: '',
            },
            submitted: false
        }
    },
    mounted() {
        axios.get('http://127.0.0.1:8000/api/departamentos/' + this.$route.params.id + '/')
            .then( response => {
                console.log(response.data)
                this.departamento = response.data
            });
    },
    methods: {
        update: function (e) {
            this.$validator.validate().then(result => {
                this.submitted = true;
                if (!result) {
                    return;
                }
                axios.put(`http://127.0.0.1:8000/api/departamentos/${this.departamento.id}/`,
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
