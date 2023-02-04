<?php

namespace Database\Seeders;

// use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use illuminate\Support\Str;
use Illuminate\Support\Facades\DB;

class DatabaseSeeder extends Seeder
{
    /**
     * Seed the application's database.
     *
     * @return void
     */
    public function run()
    {
       DB::table('users')->insert([
        'slug' => Str::slug(Str::random(20)),
        'username' => 'yannick',
        'email' => 'yannick@mail.com',
        'password' => '$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi', // password
        'is_admin' => true,
        'picture' => 'default.png',
        'status'=>'active',
        'created_at'=>now(),
        'updated_at'=>now()
       ]);

       \App\Models\User::factory(10)->create();
    }
}
