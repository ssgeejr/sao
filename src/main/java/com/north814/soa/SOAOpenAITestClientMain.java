package com.north814.soa;


import  com.theokanning.openai.*;

public class SOAOpenAITestClientMain{
    public static void main( String[] args ){
        System.out.println( "Hello World!" );
        
        try {
        	OpenAiService service = new OpenAiService("your_token");
        	CompletionRequest completionRequest = CompletionRequest.builder()
        	        .prompt("Somebody once told me the world is gonna roll me")
        	        .model("ada")
        	        .echo(true)
        	        .build();
        	service.createCompletion(completionRequest).getChoices().forEach(System.out::println);
        }catch(Exception ex) {
        	ex.printStackTrace();
        }
        
        
        
    }
}
