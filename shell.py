import language as lang

while True:
    text = input(">>> ")

    # text = """
    #         var1 = 5 * (3 - 1);
    #         var2 = 4 / 2 + 6;

    #         IF var1 > var2 {
    #             var1 = "Im greater";
    #         };
    #         ELIF var1 == var2 {
    #             var1 = "were the same";
    #             var2 = "were the same";
    #         };
    #         ELSE {
    #             var2 = "im greater";
    #         };
    #         """

    # text = """
    #         var1 = 1;

    #         FOR (i = 0; i < 10; i++) {
    #             var1 = var1 + i;
    #         };
    # """

    # text = """
    #         var1 = 1;
    #         var2 = 6;

    #         WHILE var1 < var2 {
    #             var1 = var1 + 1;
    #         };
    # """
    # text = """
    #         var1 = 1;
    #         var1++;
    # """

    #Function calls and declaration

    text = """
            FUNC fact(n) {
                num = 1;

                FOR (i = 1; i < n; i++){
                    num = num * i;
                };

                RETURN num
            };

            result = fact(5);
    """

    # text = """
    #     array = [2, 4, 5, 8, 9, 0];
    # """
   
    result, error = lang.run(text)

    if error:
        print(error.asString())
    else:
        print(result)
