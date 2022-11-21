import org.junit.Before;
import org.junit.Rule;
import org.junit.Test;
import org.junit.rules.TemporaryFolder;

import static org.junit.Assert.*;

import java.io.*;

public class TempFilesJUnit4Test {

    File file1, file2;

    /* This folder and the files created in it will be deleted after
     * tests are run, even in the event of failures or exceptions.
     */
    @Rule
    public TemporaryFolder folder = new TemporaryFolder();

    /* executed before every test: create temporary files */
    @Before
    public void setUp() {
        try {
            file1 = folder.newFile( "testfile1.txt" );
            file2 = folder.newFile( "testfile2.txt" );
        }
        catch( IOException ioe ) {
            System.err.println(
                "error creating temporary test file in " +
                this.getClass().getSimpleName() );
        }
    }

    /**
     *  Write to the two temporary files and run some asserts.
     */
    @Test
    public void test2TempFiles() {

        //write out data to the test files
        try {
FileWriter fw1 = new FileWriter( file1 );
BufferedWriter bw1 = new BufferedWriter( fw1 );
bw1.write( "content for file1");
bw1.close();

FileWriter fw2 = new FileWriter( file2 );
BufferedWriter bw2 = new BufferedWriter( fw2 );
            bw2.write( "content for file2" );
            bw2.close();
        }
        catch( IOException ioe ) {
            System.err.println(
                "error creating temporary test file in " +
                this.getClass().getSimpleName() );
        }

        assertTrue( file1.exists() );
        assertTrue( file2.isFile() );

        assertEquals( file1.length(), 17L );
        assertEquals( file1.length(), file2.length() );

        assertTrue( file1.getAbsolutePath().endsWith(
                        "testfile1.txt" ));
    }
}