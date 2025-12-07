import type { AxiosInstance, AxiosRequestConfig, AxiosResponse } from 'axios';  
import type { ApiRequestOptions } from './ApiRequestOptions';

type Headers = Record<string, string>;
type Middleware<T> = (value: T) => T | Promise<T>;
type Resolver<T> = (options: ApiRequestOptions<T>) => Promise<T>;

export class Interceptor<T> {
    _fns: Middleware<T>[];

    constructor() {
        this._fns = [];
    }

    eject(fn: Middleware<T>): void {
        const index = this._fns.indexOf(fn);
        if (index !== -1) {
            this._fns = [...this._fns.slice(0, index), ...this._fns.slice(index + 1)];
        }
    }

    use(fn: Middleware<T>): void {
        this._fns = [...this._fns, fn];
    }
}


