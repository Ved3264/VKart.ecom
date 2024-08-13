#!/usr/bin/env groovy

@Library('Django-vkart-library')_

pipeline {
    agent any
    stages {
        stage("versioning") {
            steps {
                script {
                    echo 'start versioning'
                    def filePath = 'version.txt'
                    def versionFile = readFile filePath
                    // Split the version into major, minor, and patch parts
                    def versionParts = versionFile.tokenize('.')
                    def major = versionParts[0].toInteger()
                    def minor = versionParts[1].toInteger()
                    def patch = versionParts[2].toInteger()

                    // Increment the patch version
                    patch += 1

                    // Create the new version
                    def newVersion = "${major}.${minor}.${patch}"
                    def dockerImage = 'ved1111/django-vkart-practise'
                    // Build and tag the new Docker image
                    def newImageTag = "${dockerImage}:${newVersion}"

                    env.IMG_TAG=newImageTag

                    writeFile file: filePath,text: newVersion
                    echo "Updated version to: ${newVersion}"
                    echo'end versionning'
                }
            }
        }
        stage("build and push image") {
            steps {
                echo "Building Docker image: ${env.IMG_TAG}"
                dockerImageBuild("${env.IMG_TAG}")
                dockerLogin()
                echo "Pushing Docker image: ${env.IMG_TAG}"
                dockerPush("${env.IMG_TAG}")
            }
        }
        stage("deploy") {
            script{
                    steps {
                    def dockerCMd="docker run -p 8000:8000 -d ${env.IMG_TAG}"
                    sshagent(['ec2-shh-key']){
                        sh "ssh -o StrictHostKeyChecking=no ec2-user@3.86.92.138 ${dockerCMd}"
                    }
                }
            }
        }
        stage("Commit and Push Changes") {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'vedgit', passwordVariable: 'TOKEN', usernameVariable: 'USER')]) {
                        // git config here for the first time run
                        sh 'git config --global user.email "pved81034@gmail.com"'
                        sh 'git config --global user.name "master"'

                        // Using the credentials securely
                        sh "git remote set-url origin https://${USER}:${TOKEN}@github.com/Ved3264/VKart.ecom.git"
                        sh 'git add .'
                        sh 'git commit -m "ci: version bump"'
                        sh 'git push origin HEAD:master'
                    }
                }
            }
        }

        
    }
}
