package com.samrt_nav;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.webkit.WebView;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity {
    EditText e1;
    public static final String EXTRA_MESSAGEm = "com.MESSAGE";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
    public void nw(View view ){
        WebView mWebView=new WebView(MainActivity.this);
        mWebView.getSettings().setJavaScriptEnabled(true);
        mWebView.getSettings();
        mWebView.loadUrl("https://docs.google.com/forms/d/e/1FAIpQLSe_DSjN7g7DanJ9kOgO0YkOw7_6KrjVrs45Hd25JzvKq8NazQ/viewform?c=0&w=1");
        setContentView(mWebView);
        /*String pass="yes";
        Intent intent = new Intent(this, New.class);
        intent.putExtra(EXTRA_MESSAGEm,pass);
        startActivity(intent);*/
    }

    public void info(View view ){
        e1=(EditText) findViewById(R.id.editText);
        String pass=e1.getText().toString();
        Intent intent = new Intent(this, Info.class);
        intent.putExtra(EXTRA_MESSAGEm,pass);
        startActivity(intent);
    }

}
