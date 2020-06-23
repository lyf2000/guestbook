<template>
    <div class="home">

        <ReviewList/>
    </div>
</template>

<script lang="ts">
    import {Component, Prop, Vue} from 'vue-property-decorator';
    import ReviewList from '../components/review/ReviewList.vue'

    @Component({
        components: {
            ReviewList
        }
    })
    export default class HelloWorld extends Vue {


    }
</script>

<style scoped>


</style>
