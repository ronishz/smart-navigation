package com.samrt_nav;

import android.app.ProgressDialog;
import android.content.Intent;
import android.net.Uri;
import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.ProtocolException;
import java.net.URL;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class Info extends AppCompatActivity {

    String grid;
    Integer uid;
    Double lat,lang;
    String name,mode,add,id,tim,tlat,tlang,gid,sid,slang,slat;

    private String TAG = MainActivity.class.getSimpleName();
    private ProgressDialog pDialog;

    public static final String EXTRA_MESSAGEm2 = "com.MESSAGE2";
    public static final String EXTRA_MESSAGEm3 = "com.MESSAGE3";
    public static final String EXTRA_MESSAGEm4 = "com.MESSAGE4";
    public static final String EXTRA_MESSAGEm5 = "com.MESSAGE5";

    ArrayList<String> Aname = new ArrayList<String>();
    ArrayList<String> Alat = new ArrayList<String>();
    ArrayList<String> Alang = new ArrayList<String>();
    ArrayList<String> Amode = new ArrayList<String>();
    private static String url = "https://raw.githubusercontent.com/ronishz/smart-navigation/master/start_location_data.json";
    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_info);
        Intent intent = getIntent();
        Bundle extras = intent.getExtras();
        id = extras.getString(MainActivity.EXTRA_MESSAGEm);
        uid = Integer.parseInt(id);
        uid=uid-1;

        new GetContacts().execute();


    }
    class GetContacts extends AsyncTask<Void, Void, Void> {

        @Override
        protected void onPreExecute() {
            super.onPreExecute();

            // Showing progress dialog
            pDialog = new ProgressDialog(Info.this);
            pDialog.setMessage("Please wait...");
            pDialog.setCancelable(false);
            pDialog.show();
        }

        @Override
        protected Void doInBackground(Void... arg0) {
            HttpHandler sh = new HttpHandler();

            // Making a request to url and getting response
            String jsonStr = sh.makeServiceCall(url);

            Log.e(TAG, "Response from url: " + jsonStr);

            if (jsonStr != null) {
                try {
                    JSONObject jsonObj = new JSONObject(jsonStr);

                    // Getting JSON Array node
                    JSONArray contacts = jsonObj.getJSONArray("dB");

                    // looping through All Contacts

                    JSONObject c = contacts.getJSONObject(uid);

                    name = c.getString("name");
                    add = c.getString("address");
                    mode = c.getString("mode");
                    tim = c.getString("time_req");
                    tlat = c.getString("latitude");
                    tlang = c.getString("longitude");
                    gid=c.getString("group_id");
                    sid=c.getString("start_id");
                    Aname.add(name);
                    Alat.add(tlat);
                    Alang.add(tlang);
                    Amode.add(mode);
                    lang=Double.parseDouble(tlang);
                    lat=Double.parseDouble(tlat);
                    slat=tlat;
                    slang=tlang;
                    for(Integer i=0;i<contacts.length();i++){
                        JSONObject c1 = contacts.getJSONObject(i);
                        if(gid.equals(c1.getString("group_id"))){
                            if(name.equals(c1.getString("name"))){}
                            else {
                                String tname = c1.getString("name");
                                String ttlat = c1.getString("latitude");
                                String ttlang = c1.getString("longitude");
                                String tmode = c1.getString("mode");
                                Aname.add(tname);
                                Alat.add(ttlat);
                                Alang.add(ttlang);
                                Amode.add(tmode);
                                if(sid.equals(c1.getString("id")));
                                {
                                    slat=c1.getString("latitude");
                                    slang=c1.getString("longitude");
                                }

                            }

                        }
                    }






                } catch (final JSONException e) {
                    Log.e(TAG, "Json parsing error: " + e.getMessage());
                    runOnUiThread(new Runnable() {
                        @Override
                        public void run() {
                            Toast.makeText(getApplicationContext(),
                                    "ID Does Not Exist" + e.getMessage(),
                                    Toast.LENGTH_LONG)
                                    .show();
                        }
                    });

                }
            } else {
                Log.e(TAG, "Couldn't get json from server.");
                runOnUiThread(new Runnable() {
                    @Override
                    public void run() {
                        Toast.makeText(getApplicationContext(),
                                "Couldn't get json from server. Check LogCat for possible errors!",
                                Toast.LENGTH_LONG)
                                .show();
                    }
                });

            }

            return null;
        }

        @Override
        protected void onPostExecute(Void result) {
            super.onPostExecute(result);
            if (pDialog.isShowing())
                pDialog.dismiss();
            TextView nm = (TextView) findViewById(R.id.textView2);
            TextView clg = (TextView) findViewById(R.id.textView4);
            TextView md= (TextView) findViewById(R.id.textView5);
            TextView tm = (TextView) findViewById(R.id.textView6);
            nm.setText(name);
            clg.setText(add);
            md.setText(mode);
            tm.setText(tim);
        }
    }
    class HttpHandler {

        private final String TAG = HttpHandler.class.getSimpleName();

        public HttpHandler() {
        }

        public String makeServiceCall(String reqUrl) {
            String response = null;
            try {
                URL url = new URL(reqUrl);
                HttpURLConnection conn = (HttpURLConnection) url.openConnection();
                conn.setRequestMethod("GET");
                // read the response
                InputStream in = new BufferedInputStream(conn.getInputStream());
                response = convertStreamToString(in);
            } catch (MalformedURLException e) {
                Log.e(TAG, "MalformedURLException: " + e.getMessage());
            } catch (ProtocolException e) {
                Log.e(TAG, "ProtocolException: " + e.getMessage());
            } catch (IOException e) {
                Log.e(TAG, "IOException: " + e.getMessage());
            } catch (Exception e) {
                Log.e(TAG, "Exception: " + e.getMessage());
            }
            return response;
        }

        private String convertStreamToString(InputStream is) {
            BufferedReader reader = new BufferedReader(new InputStreamReader(is));
            StringBuilder sb = new StringBuilder();

            String line;
            try {
                while ((line = reader.readLine()) != null) {
                    sb.append(line).append('\n');
                }
            } catch (IOException e) {
                e.printStackTrace();
            } finally {
                try {
                    is.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return sb.toString();
        }
    }
    public void mem(View view){
        Intent intent = new Intent(this, Enter_data.class);
        intent.putStringArrayListExtra(EXTRA_MESSAGEm2,Aname);
        intent.putStringArrayListExtra(EXTRA_MESSAGEm3,Alat);
        intent.putStringArrayListExtra(EXTRA_MESSAGEm4,Alang);
        intent.putStringArrayListExtra(EXTRA_MESSAGEm5,Amode);
        startActivity(intent);
    }
    public void  direction(View view){
        /*Double telat=Double.parseDouble(Alat.get(1));
        Double telang=Double.parseDouble(Alang.get(1));
        String rt="http://maps.google.com/maps?saddr="+lat+","+lang+"+to:"+telat+","+telang+"&daddr="+18.531206+","+73.855278;;
        */

        String jsonURL = "https://maps.google.com/maps?";
        final StringBuffer sBuf = new StringBuffer(jsonURL);
        sBuf.append("saddr=");
        Double tla=Double.parseDouble(slat);
        sBuf.append(tla);
        sBuf.append(',');
        Double tlan=Double.parseDouble(slang);
        sBuf.append(tlan);
        sBuf.append("&daddr=");
        sBuf.append(18.531206);
        sBuf.append(',');
        sBuf.append(73.855278);
        for(Integer j=0;j<Aname.size();j++) {
            if(tlat!=Alat.get(j) && slat!=Alat.get(j)) {
                sBuf.append("+to:");
                sBuf.append(Double.parseDouble(Alat.get(j)));
                sBuf.append(',');
                sBuf.append(Double.parseDouble(Alang.get(j)));
            }
        }

        Intent intent = new Intent(Intent.ACTION_VIEW,
                Uri.parse(sBuf.toString()));
        startActivity(intent);

    }


}
