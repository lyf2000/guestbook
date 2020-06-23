<template>
    <div class="reiewitem">
        <el-row>
            <el-col offset="8" span="8">
                <el-card class="cardd"  :body-style="{ padding: '0px' }">

                    <img v-if="reviewItem.image" :src="reviewItem.image"
                         class="image">
                    <div style="padding: 14px;">
                        <span>{{reviewItem.authorName}} ({{reviewItem.createdAt}})</span>
                        <div class="bottom clearfix">
                            <h4>{{reviewItem.text}}</h4>
                        </div>
                    </div>
                </el-card>
            </el-col>
        </el-row>
    </div>
</template>

<script lang="ts">
    import {Component, Prop, Vue} from 'vue-property-decorator';

    interface ListItemI {
        authorName: string;
        createdAt: string;
        id: number;
        text: string;
        image: string;
    }

    class ListItem implements ListItemI {
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

    @Component
    export default class ReviewItem extends Vue {
        @Prop() private reviewItem!: ListItem;


    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

    .time {
        font-size: 13px;
        color: #999;
    }

    .bottom {
        margin-top: 13px;
        line-height: 12px;
    }

    .button {
        padding: 0;
        float: right;
    }

    .image {
        /*width: auto;*/
        width: 100%;
        margin-left: auto;
        margin-right: auto;
        display: block;
    }

    .clearfix:before,
    .clearfix:after {
        display: table;
        content: "";
    }

    .clearfix:after {
        clear: both
    }

    .cardd {
        margin-bottom: 3%;
    }
</style>
