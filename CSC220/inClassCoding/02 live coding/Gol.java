/*****************************************************
* Author:	TJ Bowman
* Date:		7/29/2023
*
* Game of Life - Module 2 Live Coding
*****************************************************/

import java.io.*;
import java.util.Scanner;

class Gol {
	/**
	 * Game loop for Conway's Game of Life
	 * @param 		args - the command line arguments
	 */
    public static void main(String[] args) {
        boolean[][] board = readFile(args[0]);
    }

    /**
     * Read an input file and return a Game of Life board
     * @param		fileName - the name of the input file
     * @return		a Game of Life board represented as a 2D array of booleans
     */
    public static boolean[][] readFile(String fileName) {
    	boolean [][] board = null;
        int i = 0, size;
        try { 
            File inputFile = new File(fileName);
            Scanner fileReader = new Scanner(inputFile);
            String line;

            while (fileReader.hasNextLine()){
                line = fileReader.nextLine();
                if (i == 0){
                    size = line.length();
                    board = new boolean[size][size];
                }

                fillRow(board, line, i);
                i++;
            }
            fileReader.close();
        } catch (Exception e) {}
        return board;
    }

    /**
     * Given a board, line from the input file, and board row number,
     * fill in that line of the board
     * @param		board - a Game of Life board
     * @param		line - a single line from the input file
     * @param		row - a row number for the board
     */
    public static void fillRow(boolean[][] board, String line, int row) {
        for (int i = 0; i < line.length(); i++){
            board[row][i] = (line.charAt(i) == '*') ? true : false;
        }
	}

	/**
	 * Display the current game board
	 * @param		gen - the current game generation number
	 * @param		board - the curent Game of Life board
	 */
    public static void printBoard(int gen, boolean[][] board) {

    }

	/**
	 * Given a cell on the board, return its number of neighbors
	 * @param		board - a Game of Life board
	 * @param		row - a row number from the board
	 * @param		col - a column number from the board
	 * @return		the number of neighbors of the cell at row & col
	 */
	public static int countNeighbours(boolean[][] board, int row, int col) {
		return -1;
    }

    /**
     * Update the game board to the next generation
     * @param		board - the current Game of Life board
     * @return		the next generation Game of Life board
     */
    public static boolean[][] playGame(boolean[][] board) {
    	return null;
    }

    /***********************************
    ********** HELPER METHODS **********
    ***********************************/

    /**
     * Clear the console (on Windows machines)
     */
    public static void cls() {

    }

    /**
     * Halt program execution (sleep) for some number of milliseconds
     * @param		duration - the length of time in milliseconds to sleep
     */
    public static void mySleep(int duration) {

    }
}