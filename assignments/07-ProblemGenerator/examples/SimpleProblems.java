package codegen;

import java.io.IOException;
import java.util.Scanner;

import javax.lang.model.element.Modifier;
import com.squareup.javapoet.JavaFile;
import com.squareup.javapoet.MethodSpec;
import com.squareup.javapoet.TypeSpec;

public class SimpleProblems {
	public static void main(String[] args) throws IOException {

		Scanner scan = new Scanner(System.in);
		System.out.print("Enter what should be printed: ");
		String answer = scan.next();
		scan.close();
		System.out.println("\n");
		
		MethodSpec main = MethodSpec.methodBuilder("main")
				.addModifiers(Modifier.PUBLIC, Modifier.STATIC)
				.returns(void.class)
				.addParameter(String[].class, "args")
				.addStatement("$T.out.println($S)", System.class, answer)
				.build();

		TypeSpec test = TypeSpec.classBuilder("Test")
				.addModifiers(Modifier.PUBLIC)
				.addMethod(main)
				.addJavadoc("What is printed by the following code?")
				.build();

		JavaFile javaFile = JavaFile.builder("", test)
				.build();

		javaFile.writeTo(System.out);	
	}
}
