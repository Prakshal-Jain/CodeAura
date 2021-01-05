'use strict';

import browserSync from 'browser-sync';
import del from 'del';
import path from 'path';
import gulp from 'gulp';
import named from 'vinyl-named';
import yargs from 'yargs';


var sass = require('gulp-dart-sass');
const sourceMaps = require('gulp-sourcemaps');
const autoprefixer = require('gulp-autoprefixer');
const uglify = require('gulp-uglify');
const cleanCss = require('gulp-clean-css');
const gulpif = require('gulp-if');
const imagemin = require('gulp-imagemin');

const PRODUCTION = !!yargs.argv.p;
const _STATIC = path.resolve('static');
const _NODE_MODULES = path.resolve('node_modules');

//  paths
const PATHS = {
  src: {
    base: path.join(_STATIC, 'src'),
    images: path.join(_STATIC, 'src', 'img'),
    scripts: path.join(_STATIC, 'src', 'js'),
    styles: path.join(_STATIC, 'src', 'scss'),
    stylesCss: path.join(_STATIC, 'src', 'css'),
  },
  dest: {
    base: path.join(_STATIC, 'dist'),
    images: path.join(_STATIC, 'dist', 'img'),
    scripts: path.join(_STATIC, 'dist', 'js'),
    styles: path.join(_STATIC, 'dist', 'css'),
  },
};


function browserSyncServer(c) {
  browserSync.init({ proxy: 'localhost:8000' });
  c();
}

function cleanDist() {
  return del(path.join(PATHS.dest.base, '**'));
}

function sassCompile() {
  return gulp
    .src(path.join(PATHS.src.styles, '**', '*'))
    .pipe(gulpif(!PRODUCTION, sourceMaps.init()))
    .pipe(sass().on('error', sass.logError))
    .pipe(autoprefixer())
    .pipe(gulpif(PRODUCTION, cleanCss({ compatibility: 'ie9' })))
    .pipe(gulpif(!PRODUCTION, sourceMaps.write()))
    .pipe(gulp.dest(PATHS.dest.styles))
    .pipe(browserSync.stream());
}

function cssCompile(){
  return gulp
    .src(path.join(PATHS.src.stylesCss, '**', '*'))
    .pipe(gulpif(!PRODUCTION, sourceMaps.init()))
    .pipe(autoprefixer())
    .pipe(gulpif(PRODUCTION, cleanCss({ compatibility: 'ie9' })))
    .pipe(gulpif(!PRODUCTION, sourceMaps.write()))
    .pipe(gulp.dest(PATHS.dest.styles))
    .pipe(browserSync.stream());
}

function images() {
  return gulp
    .src(path.join(PATHS.src.images, '**', '*'))
    .pipe(imagemin())
    .pipe(gulp.dest(PATHS.dest.images));
}

function scripts() {
  return (
    gulp
      .src(path.join(PATHS.src.scripts, '**', '*.js'))
      .pipe(named())
      .pipe(gulpif(!PRODUCTION, sourceMaps.init()))
      .pipe(gulpif(PRODUCTION, uglify()))
      .pipe(gulpif(!PRODUCTION, sourceMaps.write()))
      .pipe(gulp.dest(PATHS.dest.scripts))
  );
}

function others(c) {
  // console.log('others');
  c();
}

function watchChanges() {
  gulp
    .watch(path.join(path.resolve('templates'), '**', '*'))
    .on('all', browserSync.reload);
  gulp
    .watch(path.join(PATHS.src.images, '**', '*'))
    .on('all', gulp.series(images, browserSync.reload));
  gulp
    .watch(path.join(PATHS.src.scripts, '**', '*'))
    .on('all', gulp.series(scripts, browserSync.reload));
  gulp.watch(path.join(PATHS.src.styles, '**', '*')).on('all', gulp.series(sassCompile,browserSync.reload));
  gulp.watch(path.join(PATHS.src.stylesCss, '**', '*')).on('all', gulp.series(cssCompile,browserSync.reload));
}

gulp.task(
  'build',
  gulp.series(cleanDist, gulp.parallel(scripts, sassCompile, others,cssCompile ,images))
);

gulp.task('watch', gulp.series('build', browserSyncServer, watchChanges));
