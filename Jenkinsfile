#!/usr/bin/env groovy

@Library('Django-vkart-library')_

pipeline {
    agent any
    stages {
        stage("versioning") {
            steps {
                def currentVersion = new File('version.txt').text.trim()

                if (!currentVersion) {
                    throw new RuntimeException("Current version is not available")
                }
                def versionParts = currentVersion.tokenize('.')
                def major = versionParts[0].toInteger()
                def minor = versionParts[1].toInteger()
                def patch = versionParts[2].toInteger()
                // Increment the patch version
                patch += 1
                // Create the new version
                def newVersion = "${major}.${minor}.${patch}"
                // Optionally, update the version in the file
                new File('version.txt').text = newVersion
                println "Updated version to: ${newVersion} in file"
            }
        }
        stage("test") {
            steps {
                echo "test success"
            }
        }
        stage("build and push image") {
            steps {
                dockerImageBuild 'ved1111/django-app-practise:1.3'
                dockerLogin()
                dockerPush 'ved1111/django-app-practise:1.3'
            }
        }
        stage("deploy") {
            steps {
                echo 'deploy successfully'
            }
        }
        stage("git update") {
            steps {
                gitPush()
            }
        }
    }
}
