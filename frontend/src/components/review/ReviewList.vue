<template>
    <div class="hello">
        <p>Hiiii</p>

        <ReviewItem v-for="review of m" :key="review.id" :review-item="review"/>

    </div>
</template>

<script lang="ts">
    import {Component, Prop, Vue} from 'vue-property-decorator';
    import ReviewItem from '@/components/review/ReviewItem.vue'


    interface ListItemI {
        authorName: string;
        createdAt: string;
        id: number;
        text: string;
    }

    class ListItem implements ListItemI {
        authorName: string;
        createdAt: string;
        id: number;
        text: string;

        constructor(authorName: string, createdAt: string, id: number, text: string) {
            this.authorName = authorName;
            this.createdAt = createdAt;
            this.id = id;
            this.text = text;
        }
    }

    @Component({
        components: {
            ReviewItem
        }
    })
    export default class ReviewList extends Vue {
        m: ListItem[] = [];

        created() {
            this.getReviewList()
        }

        ajaxGet(url: string, callback: any): void {
            this.$http.get(url)
                .then(response => {
                    callback(response.data)
                })
        }

        getReviewList(): void {
            this.loadReviewList()
        }

        newList(data: any[]): void {
            console.log('newList', data)
            data.forEach(value => {
                const authorName: string = value['author_name']
                const createdAt: string = value['created_at']
                const id: number = value['id']
                const text: string = value['text']
                this.m.push(new ListItem(authorName, createdAt, id, text))
            })
        }

        loadReviewList(): void {
            this.ajaxGet('reviews', this.newList)
        }


    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>


</style>
