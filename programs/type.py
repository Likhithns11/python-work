def ec2():
    ec2Instance = [
                    {
                        "id" : "ec001",
                        "typ" : "t2micro"
                    },
                    {
                        "id" : "ec002",
                        "typ" : "t2medium"
                    },
                    {
                        "id" : "ec003",
                        "typ" : "t3large"
                    }
                  ]
    print(ec2Instance[1]["typ"])

ec2()
    