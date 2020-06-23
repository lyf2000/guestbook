<template>
    <div class="reiewitem">
        <el-row>
            <el-col offset="4" span="16">
                <el-card :body-style="{ padding: '0px' }">
                    <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png"
                         class="image">
                    <div style="padding: 14px;">
                        <span>{{reviewItem.id}}</span>
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
        width: auto;
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

</style>
