pipeline{
        agent any
        stages{
            stage('Testing'){
                steps{
                    sh "./scripts/test.sh"
                }
            }
            stage('Build'){
                steps{
                    sh "./scripts/build-images.sh"
                }
            }
            stage('Deploy App'){
                steps{
                    sh "./scripts/run.sh"
                }
            }
        }
}