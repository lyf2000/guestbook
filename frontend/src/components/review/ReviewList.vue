<template>
    <div class="hello">
        <p>Hiiii</p>
        <el-button
                @click="getReviewList"

        />
    </div>
</template>

<script lang="ts">
    import {Component, Prop, Vue} from 'vue-property-decorator';
    import th from "element-ui/src/locale/lang/th";

    interface ListItem {
        id: number;
        author_name: string;
        text: string;
        created_at: string;
    }


    @Component
    export default class ReviewList extends Vue {
        m: any = [];

        created() {
            // this.getReviewList()
        }

        ajaxGet(url: string, callback: any): object {
            this.$http.get(url)
                .then(response => {
                    callback(response.data)
                })
        }

        getReviewList(): void {
            this.loadReviewList()
        }

        newList(data: any): void {
            console.log('newList', data)
            this.m = data
        }

        loadReviewList(): void {
            console.log(123)
            this.ajaxGet('reviews', this.newList)
        }


    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>


</style>
