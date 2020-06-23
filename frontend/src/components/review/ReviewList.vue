<template>
    <div class="hello">
        <p>Hiiii</p>

        <ReviewCreateForm @new-review="newReivew"/>

        <ReviewItem v-for="review of reviewList" :key="review.id" :review-item="review"/>

    </div>
</template>

<script lang="ts">
    import {Component, Prop, Vue} from 'vue-property-decorator';
    import ReviewItem from '@/components/review/ReviewItem.vue'
    import ReviewCreateForm from '@/components/review/ReviewCreateForm.vue'


    interface ReviewI {
        authorName: string;
        createdAt: string;
        id: number;
        text: string;
        image: string;
    }

    class Review implements ReviewI {
        authorName: string;
        createdAt: string;
        id: number;
        text: string;
        image: string;

        constructor(authorName: string, createdAt: string, id: number, text: string, image: string) {
            this.authorName = authorName;
            this.createdAt = createdAt;
            this.id = id;
            this.text = text;
            this.image = image;
        }
    }

    @Component({
        components: {
            ReviewItem, ReviewCreateForm
        }
    })
    export default class ReviewList extends Vue {
        reviewList: Review[] = [];

        created() {
            this.getReviewList()
        }

        newReivew(review: Review) {
            this.reviewList.unshift(review)
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
                const image: string = value['image']
                this.reviewList.push(new Review(authorName, createdAt, id, text, image))
            })
        }

        loadReviewList(): void {
            this.ajaxGet('reviews', this.newList)
        }


    }
</script>

<style scoped>


</style>
