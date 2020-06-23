<template>
    <div class="reviewcreateform">

        <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="120px" class="demo-ruleForm">
            <el-form-item label="Name" prop="name">
                <el-input type="text" v-model="ruleForm.name" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="Text" prop="text">
                <el-input type="text" v-model="ruleForm.text" autocomplete="off"></el-input>
            </el-form-item>


            <!--            <el-upload-->
            <!--                    :file-list="ruleForm.image"-->
            <!--                    ref="upload"-->
            <!--                    action="."-->
            <!--                    :auto-upload="false">-->
            <!--                <el-button slot="trigger" size="small" type="primary">select file</el-button>-->
            <!--            </el-upload>-->


            <el-form-item>
                <el-button type="primary" @click="submitForm('ruleForm')">Submit</el-button>
                <el-button @click="resetForm('ruleForm')">Reset</el-button>
            </el-form-item>
        </el-form>

    </div>
</template>


<script lang="ts">
    import {Component, Prop, Vue, Emit} from 'vue-property-decorator';
    import fi from "element-ui/src/locale/lang/fi";

    interface RuleFormI {
        name: string;
        text: string;
        image: any;
    }

    class RuleForm implements RuleFormI {
        name: string;
        text: string;
        image: any;

        constructor(name: string, text: string, image: any) {
            this.name = name;
            this.text = text;
            this.image = image;
        }
    }

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
    export default class ReviewCreateForm extends Vue {

        ruleForm = new RuleForm('', '', '')
        validators = {
            validateName: (rule: object, value: string, callback: any) => {
                if (value === '') {
                    callback(new Error('Please input the name'));
                } else {
                    if (value.length < 3 || value.length > 32) {
                        callback(new Error('[3; 32]'));
                    }
                    callback();
                }
            },
            validateText: (rule: object, value: string, callback: any) => {
                if (value === '') {
                    callback(new Error('Please input the name'));
                } else {
                    if (value.length < 16 || value.length > 512) {
                        callback(new Error('[16; 512]'));
                    }
                    callback();
                }
            },
            // validatePass2: (rule, value, callback) => {
            //     if (value === '') {
            //         callback(new Error('Please input the password again'));
            //     } else if (value !== this.ruleForm.pass) {
            //         callback(new Error('Two inputs don\'t match!'));
            //     } else {
            //         callback();
            //     }
            // }
        }
        errorMessage = {
            'author_name': 'Name',
            'text': 'Text'
        }

        submitUpload() {
            this.$refs.upload.submit();
        }

        resetForm(formName: string) {
            this.$refs[formName].resetFields();
        }


        submitForm(formName: string) {
            this.$refs[formName].validate((valid) => {
                if (valid) {
                    console.log(this.ruleForm.image)
                    console.log(typeof this.ruleForm.image)
                    this.createReview()
                } else {
                    console.log('error submit!!');
                    return false;
                }
            });
        }

        createReview() {
            const formData = new FormData();
            formData.append("text", this.ruleForm.text);
            formData.append("author_name", this.ruleForm.name);
            formData.append("image", this.ruleForm.image);

            console.log(formData)

            this.ajaxPost('reviews/', formData)
                .then(response => {
                    const value = response.data
                    const authorName: string = value['author_name']
                    const createdAt: string = value['created_at']
                    const id: number = value['id']
                    const text: string = value['text']
                    const image: string = value['image']
                    this.$emit('new-review', new ListItem(authorName, createdAt, id, text, image))
                })
                .catch(response => {
                    console.log('err')
                    this.getError(response.response)

                })
        }

        getError(response) {
            const data = response.data
            let message = '';
            console.log(data)
            for (const [key, value] of Object.entries(data)) {
                message += `${this.errorMessage[key]}: ${value}`
            }

            alert(message)
        }

        ajaxPost(url: string, data: object) {
            const d = {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            }
            return this.$http.post(url, data, d)
        }


        rules = {
            // pass: [
            //     {validator: this.validators['validatePass'], trigger: 'blur'}
            // ],
            // checkPass: [
            //     {validator: this.validators['validatePass2'], trigger: 'blur'}
            // ],
            // age: [
            //     {validator: this.validators['checkAge'], trigger: 'blur'}
            // ],
            name: [
                {validator: this.validators['validateName'], trigger: 'blur'}
            ],
            text: [
                {validator: this.validators['validateText'], trigger: 'blur'}
            ]
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>


</style>
