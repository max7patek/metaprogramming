package codegen;

import java.io.IOException;
import java.util.Scanner;

import javax.lang.model.element.Modifier;

import com.squareup.javapoet.JavaFile;
import com.squareup.javapoet.MethodSpec;
import com.squareup.javapoet.TypeSpec;

public class PassByReferenceProblems {

	public static void main(String[] args) throws IOException {
		Scanner scan = new Scanner(System.in);
		System.out.print("Enter what should be printed: ");
		String answer = scan.next();
		scan.close();
		System.out.println("\n");
		
		if (answer.length() < 3) 
			throw new IllegalArgumentException("Answer String must be at least 3 characters.");
		
		String p1 = answer.substring(0, answer.length()-2);
		String p2 = ""+answer.charAt(answer.length()-2);
		String p3 = ""+(char)(answer.charAt(answer.length()-1)-1);
		if (!(Character.isDigit(p3.charAt(0)) 
						|| Character.isLetter(p3.charAt(0))))
			throw new IllegalArgumentException("Illegal last character.");
		
		
		MethodSpec foo = MethodSpec.methodBuilder("foo")
				.addModifiers(Modifier.PUBLIC, Modifier.STATIC)
				.returns(void.class)
				.addParameter(String.class, "s")
				.addParameter(char.class, "c")
				.addParameter(char[].class, "a")
				.addStatement("s += $S", "!")
				.addStatement("c++")
				.addStatement("a[0]++")
				.build();
				
		
		MethodSpec main = MethodSpec.methodBuilder("main")
				.addModifiers(Modifier.PUBLIC, Modifier.STATIC)
				.returns(void.class)
				.addParameter(String[].class, "args")
				.addStatement("String s = $S", p1)
				.addStatement("char c = $S", p2)
				.addStatement("char[] a = {$S}", p3)
				.addStatement("$N(s, c, a)", foo)
				.addStatement("$T.out.println(s + c + a[0])", System.class)
				.build();
		
		

		TypeSpec test = TypeSpec.classBuilder("Test")
				.addModifiers(Modifier.PUBLIC)
				.addMethod(main)
				.addMethod(foo)
				.addJavadoc("What is printed by the following code?")
				.build();

		JavaFile javaFile = JavaFile.builder("", test)
				.build();

		javaFile.writeTo(System.out);	
	}

}
